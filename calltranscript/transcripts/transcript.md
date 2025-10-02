Here’s a **detailed incident call transcript in Markdown** with **precise timestamps, speaker tags, and severity updates**:

---

# **Incident Call Transcript**
**Meeting Title:** Sev-1 Incident Bridge – API Gateway Outage  
**Date:** 2025-10-02  
**Duration:** 45 minutes  
**Participants:**  
- **Aveek Roy Chowdhury** – Cloud Solution Architect  
- **Amie Fleming** – Incident Manager  
- **Adam Turner** – SRE Lead  
- **Robyn Thelander** – Support Engineer  

---

## **Agenda**
- Diagnose root cause of API Gateway outage  
- Execute mitigation steps and confirm recovery  
- Assign follow-up actions and next steps  

---

## **Detailed Transcript**

**00:00[1]() Amie Fleming (Incident Manager):**  
Welcome, everyone. This is a **Sev-1** impacting multiple customers. API Gateway requests are timing out globally. Let’s start with status updates.

---

**02:15[2]() Adam Turner (SRE Lead):**  
Confirmed. Latency spiked at **11:45 AM UTC**. East US region is the most impacted. Other regions show minor degradation.

---

**04:30[3]() Aveek Roy Chowdhury (Cloud Solution Architect):**  
Checked **Azure Monitor** logs. Seeing a surge in **502 Bad Gateway errors**. Health probes for backend pools are failing.

---

**06:50[4]() Robyn Thelander (Support Engineer):**  
Found a **config change** deployed at **11:30 AM UTC** to load balancer rules. Likely culprit. Initiating rollback now.

---

**08:10[5]() Amie Fleming:**  
Good catch. Robyn, ETA for rollback?

---

**08:25[6]() Robyn Thelander:**  
Approximately **10 minutes**.

---

**15:00[7]() Adam Turner:**  
Rollback completed. Monitoring traffic. Latency trending down. East US stabilizing.

---

**18:30[8]() Aveek Roy Chowdhury:**  
Confirmed. No new 502 errors in the last **5 minutes**. Error rate back to baseline.

---

**20:00[9]() Amie Fleming:**  
Great. Let’s keep the bridge open for **15 more minutes** to confirm stability.

---

**35:00[10]() Adam Turner:**  
All metrics normal across regions. Declaring **incident mitigated**.

---

**40:00[11]() Amie Fleming:**  
Closing the bridge. Thanks, everyone. Post-incident review scheduled for tomorrow.

---

## **Root Cause**
Misconfigured load balancer rule introduced during routine maintenance caused health probe failures, leading to API Gateway timeouts.

---

## **Mitigation**
Rollback of the faulty configuration resolved the issue.

---

## **Action Items**
- **Adam Turner:** Implement automated validation for load balancer rule changes (**Due: Oct 10**)  
- **Aveek Roy Chowdhury:** Update incident runbook with new validation steps (**Due: Oct 12**)  
- **Robyn Thelander:** Share post-incident report with leadership (**Due: Oct 15**)  

---

✅ Do you want me to **create a reusable Markdown template for all future incident calls** (with placeholders for timestamps, severity, participants, and action items), or should I **generate a second example for a different type of incident (e.g., database outage)**?