import streamlit as st
import plotly.express as px
from utils.db import fetch_df, init_db
from utils.state import init_session
from agents.marketing_agents import campaign_health_agent

init_db(); init_session()
st.title("📈 Campaign Health Monitor")

camps = fetch_df("SELECT * FROM campaigns")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Avg CTR", f"{camps['ctr'].mean():.2f}%")
c2.metric("Avg CPC", f"${camps['cpc'].mean():.2f}")
c3.metric("Avg Conv Rate", f"{camps['conv_rate'].mean():.2f}%")
c4.metric("Avg Bounce", f"{camps['bounce_rate'].mean():.1f}%")

st.subheader("Performance Heatmap")
metrics = camps[["name", "ctr", "cpc", "conv_rate", "bounce_rate"]].set_index("name")
st.plotly_chart(px.imshow(metrics.T, aspect="auto", color_continuous_scale="RdYlGn"),
                use_container_width=True)

st.subheader("CTR vs Conversion Rate")
st.plotly_chart(px.scatter(camps, x="ctr", y="conv_rate", size="spend",
                           color="channel", hover_name="name"),
                use_container_width=True)

# Alerts
st.subheader("🚨 Alerts")
alerts = []
for _, r in camps.iterrows():
    if r["ctr"] < 2: alerts.append(f"⚠️ **{r['name']}** low CTR ({r['ctr']}%)")
    if r["bounce_rate"] > 60: alerts.append(f"⚠️ **{r['name']}** high bounce ({r['bounce_rate']}%)")
    if r["cpc"] > 5: alerts.append(f"⚠️ **{r['name']}** high CPC (${r['cpc']})")
if alerts:
    for a in alerts[:10]: st.warning(a)
else:
    st.success("All campaigns healthy ✅")

st.divider()
if st.button("🤖 Run AI Campaign Health Analysis"):
    with st.spinner("AI analyzing..."):
        st.markdown(campaign_health_agent())
