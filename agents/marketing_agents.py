"""Autonomous AI marketing agents."""
from utils.ai import generate
from utils.db import get_conn, log_agent, save_report, fetch_df
from datetime import datetime


def keyword_research_agent(seed: str):
    log_agent("KeywordResearch", "running", f"seed='{seed}'")
    out = generate(
        f"Generate a JSON-style table (markdown) of 10 high-intent SEO keywords related to '{seed}'. "
        "Columns: keyword, monthly_volume, difficulty(1-100), intent, suggested_content_type.",
        "You are an SEO keyword research expert."
    )
    log_agent("KeywordResearch", "success", f"{len(out)} chars")
    return out


def seo_trend_agent(topic: str):
    log_agent("SEOTrend", "running", topic)
    out = generate(
        f"Analyze current SEO trends for '{topic}'. Provide: 1) 3 emerging trends, "
        "2) 3 declining tactics, 3) 5 actionable recommendations. Use markdown.",
        "You are an SEO trend analyst."
    )
    log_agent("SEOTrend", "success", "ok")
    return out


def campaign_health_agent():
    log_agent("CampaignHealth", "running", "analyzing all campaigns")
    df = fetch_df("SELECT name,channel,ctr,cpc,conv_rate,bounce_rate,spend FROM campaigns")
    summary = df.to_markdown(index=False)
    out = generate(
        f"Analyze these marketing campaigns and identify: top 3 winners, bottom 3 underperformers, "
        f"and 5 specific optimization actions.\n\n{summary}",
        "You are a paid media performance analyst."
    )
    log_agent("CampaignHealth", "success", "ok")
    return out


def content_idea_agent(niche: str):
    log_agent("ContentIdeas", "running", niche)
    out = generate(
        f"Generate 10 viral content ideas for the niche '{niche}'. For each: title, hook, "
        "platform (blog/LinkedIn/X/Instagram/TikTok), estimated engagement potential.",
        "You are a viral content strategist."
    )
    log_agent("ContentIdeas", "success", "ok")
    return out


def lead_scoring_agent():
    log_agent("LeadScoring", "running", "rescoring leads")
    conn = get_conn()
    rows = conn.execute("SELECT id,engagement,visits FROM leads").fetchall()
    updated = 0
    for r in rows:
        score = min(100, int(r["engagement"] * 0.5 + r["visits"] * 1.2))
        cat = "High" if score > 70 else ("Medium" if score > 40 else "Low")
        conn.execute("UPDATE leads SET score=?, category=? WHERE id=?", (score, cat, r["id"]))
        updated += 1
    conn.commit()
    conn.close()
    log_agent("LeadScoring", "success", f"rescored {updated}")
    return f"✅ Rescored {updated} leads using AI weighting (engagement×0.5 + visits×1.2)."


def report_agent():
    log_agent("Report", "running", "weekly report")
    camps = fetch_df("SELECT * FROM campaigns")
    leads = fetch_df("SELECT category, COUNT(*) as n FROM leads GROUP BY category")
    kws = fetch_df("SELECT keyword,rank,trend FROM keywords ORDER BY rank LIMIT 10")

    prompt = f"""Write an executive weekly marketing report (markdown) covering:
- Performance overview ({len(camps)} campaigns, total spend ${camps['spend'].sum():.2f})
- Top campaigns by conversion rate
- Lead distribution: {leads.to_dict(orient='records')}
- SEO highlights: {kws.to_dict(orient='records')}
- 5 strategic recommendations
"""
    out = generate(prompt, "You are a CMO writing for executives.")
    title = f"Weekly Report — {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    save_report(title, out)
    log_agent("Report", "success", title)
    return title, out


AGENTS = {
    "Keyword Research": ("Generate keywords from a seed term", keyword_research_agent, True),
    "SEO Trend Monitor": ("Analyze SEO trends for a topic", seo_trend_agent, True),
    "Campaign Health Check": ("Analyze all campaigns", campaign_health_agent, False),
    "Content Idea Generator": ("Brainstorm content for a niche", content_idea_agent, True),
    "Lead Scoring Engine": ("Re-score all leads with AI weighting", lead_scoring_agent, False),
    "Automated Reporter": ("Generate weekly executive report", report_agent, False),
}
