"""SQLite-based lightweight database for campaigns, leads, keywords, reports, logs."""
import sqlite3
import os
from datetime import datetime, timedelta
import random

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "marketing.db")


def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS campaigns(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, channel TEXT, status TEXT,
        impressions INTEGER, clicks INTEGER, conversions INTEGER,
        spend REAL, ctr REAL, cpc REAL, conv_rate REAL, bounce_rate REAL,
        created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS keywords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT, volume INTEGER, difficulty INTEGER,
        rank INTEGER, trend TEXT, updated_at TEXT
    );
    CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, email TEXT, source TEXT,
        engagement INTEGER, visits INTEGER, score INTEGER,
        category TEXT, created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT, content TEXT, type TEXT, created_at TEXT
    );
    CREATE TABLE IF NOT EXISTS agent_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent TEXT, status TEXT, message TEXT, created_at TEXT
    );
    """)
    conn.commit()

    # Seed if empty
    if c.execute("SELECT COUNT(*) FROM campaigns").fetchone()[0] == 0:
        seed_demo_data(conn)
    conn.close()


def seed_demo_data(conn):
    c = conn.cursor()
    channels = ["Google Ads", "Meta Ads", "LinkedIn", "TikTok", "Email", "SEO"]
    for i in range(12):
        imp = random.randint(5000, 80000)
        clk = int(imp * random.uniform(0.02, 0.08))
        conv = int(clk * random.uniform(0.03, 0.12))
        spend = round(random.uniform(200, 5000), 2)
        c.execute("""INSERT INTO campaigns(name,channel,status,impressions,clicks,conversions,spend,ctr,cpc,conv_rate,bounce_rate,created_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", (
            f"Campaign {i+1}", random.choice(channels),
            random.choice(["active", "active", "active", "paused"]),
            imp, clk, conv, spend,
            round(clk/imp*100, 2), round(spend/max(clk,1), 2),
            round(conv/max(clk,1)*100, 2), round(random.uniform(20, 70), 2),
            (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        ))

    kws = ["ai marketing", "seo automation", "content generation", "lead scoring",
           "marketing ai agents", "growth hacking", "ppc optimization", "email automation",
           "keyword research", "campaign analytics", "ad copy ai", "marketing dashboard"]
    for k in kws:
        c.execute("""INSERT INTO keywords(keyword,volume,difficulty,rank,trend,updated_at)
            VALUES(?,?,?,?,?,?)""", (
            k, random.randint(500, 50000), random.randint(20, 90),
            random.randint(1, 50), random.choice(["↑", "↓", "→"]),
            datetime.now().isoformat()
        ))

    sources = ["Organic", "Paid Search", "Social", "Referral", "Email"]
    for i in range(40):
        eng = random.randint(1, 100)
        vis = random.randint(1, 50)
        score = min(100, int(eng * 0.5 + vis * 1.2 + random.randint(0, 20)))
        cat = "High" if score > 70 else ("Medium" if score > 40 else "Low")
        c.execute("""INSERT INTO leads(name,email,source,engagement,visits,score,category,created_at)
            VALUES(?,?,?,?,?,?,?,?)""", (
            f"Lead {i+1}", f"lead{i+1}@example.com",
            random.choice(sources), eng, vis, score, cat,
            (datetime.now() - timedelta(hours=random.randint(0, 240))).isoformat()
        ))
    conn.commit()


def log_agent(agent, status, message):
    conn = get_conn()
    conn.execute("INSERT INTO agent_logs(agent,status,message,created_at) VALUES(?,?,?,?)",
                 (agent, status, message, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def save_report(title, content, rtype="markdown"):
    conn = get_conn()
    conn.execute("INSERT INTO reports(title,content,type,created_at) VALUES(?,?,?,?)",
                 (title, content, rtype, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def fetch_df(query, params=()):
    import pandas as pd
    conn = get_conn()
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df
