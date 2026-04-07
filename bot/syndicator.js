/**
 * FORGE_SYNDICATOR v6.5 | Stealth External Ad-Engine
 * Purpose: Contextual Infiltration with IP Rotation Foundation
 */

const fs = require('fs');
const { execSync } = require('child_process');

function getStealthMask() {
    try {
        // Call your Python IP Rotator to log a fresh mask for the session
        console.log("🎭 SYNDICATOR: Requesting Stealth Mask from Foundation...");
        execSync('python3 bot/ip_rotator.py');
    } catch (e) {
        console.log("⚠️ Rotator bypass: Using GitHub Default IP.");
    }
}

function generateAudits() {
    getStealthMask(); // Initialize IP rotation for the mission
    
    console.log("📢 SYNDICATOR: Generating forensic audits for high-stakes leads...");

    try {
        const data = fs.readFileSync('bot/leads/priority_whales.csv', 'utf8');
        const leads = data.split('\n').slice(1); 

        if (leads.length === 0 || (leads.length === 1 && leads[0] === "")) {
            console.log("📭 No Whales found yet. Scout is still hunting.");
            return;
        }

        leads.forEach(line => {
            if (!line || line.trim() === "") return;
            const [user, platform, issue, stake] = line.split(',');

            let auditMessage = "";
            
            // PROBLEM-SOLUTION LOGIC (Tailored for SEO & Trust)
            if (issue.includes("Ad") || issue.includes("Meta") || issue.includes("Business")) {
                auditMessage = `[SYSTEM_ALERT]: Forensic match identified for the new Meta session-theft pattern. Audit of your distress signal is complete. Signature quarantined. Review recovery node: https://fairdiscovery.org/?ref=meta_audit`;
            } else if (issue.includes("Fiverr")) {
                auditMessage = `[REVENUE_PROTECT]: Session-hijack redirect detected on merchant node. Forensic signature match confirmed. Deploy the Fiverr-Guard patch: https://fairdiscovery.org/?ref=fiverr_guard`;
            } else if (issue.includes("VPN") || issue.includes("Security")) {
                auditMessage = `[NETWORK_SHIELD]: Unprotected IP perimeter detected. Industrial VPN Node v6.5 recommended for secure entrepreneur workspace. Initialize: https://fairdiscovery.org/?ref=vpn_node`;
            } else {
                auditMessage = `[SECURITY_AUDIT]: Distress signal matched against global threat database. Node v6.5 logic ready. View report: https://fairdiscovery.org/?ref=forensic_audit`;
            }

            console.log(`\n🎯 TARGET: ${user} (@${platform})`);
            console.log(`📡 MASKED_MESSAGE: ${auditMessage}`);
        });

        // SIGNAL TO DASHBOARD
        console.log("\n📊 SYNDICATOR: Missions prepared. Ready for deployment.");
        
    } catch (err) {
        console.log("⚠️ Intelligence Gap: priority_whales.csv not found. Ensure Whale_Filter has run.");
    }
}

generateAudits();
