/**
 * FORGE_SYNDICATOR v6.4 | External Ad-Engine
 * Purpose: Contextual Infiltration & Backlink Generation
 */

const fs = require('fs');

function generateAudits() {
    console.log("📢 SYNDICATOR: Generating external forensic audits...");

    // Read the latest high-value leads from the Whale Filter
    try {
        const data = fs.readFileSync('bot/leads/priority_whales.csv', 'utf8');
        const leads = data.split('\n').slice(1); // Skip header

        leads.forEach(line => {
            if (!line) return;
            const [user, platform, issue, stake] = line.split(',');

            // THE PROBLEM-SOLUTION LOGIC
            let auditMessage = "";
            let refCode = issue.toLowerCase().replace(/\s+/g, '_');

            if (issue.includes("Ad") || issue.includes("Meta")) {
                auditMessage = `[SYSTEM_ALERT]: Forensic match identified for the new Meta session-theft pattern. Audit of your recent distress signal is complete. Signature quarantined. Review the recovery node here: https://fairdiscovery.org/?ref=meta_audit`;
            } else if (issue.includes("Fiverr")) {
                auditMessage = `[REVENUE_PROTECT]: Session-hijack redirect detected on current merchant node. Forensic signature match confirmed. Deploy the Fiverr-Guard patch immediately: https://fairdiscovery.org/?ref=fiverr_guard`;
            } else {
                auditMessage = `[SECURITY_AUDIT]: Distress signal matched against global threat database. Node v6.4 logic ready for deployment. View audit report: https://fairdiscovery.org/?ref=forensic_audit`;
            }

            console.log(`\n🚀 TARGET: ${user} on ${platform}`);
            console.log(`📝 MESSAGE: ${auditMessage}`);
        });
    } catch (err) {
        console.log("⚠️ Waiting for Whale Filter to populate priority_whales.csv...");
    }
}

generateAudits();
