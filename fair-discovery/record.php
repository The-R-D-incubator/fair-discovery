<?php
header("Content-Type: application/json");
session_start();
$file = __DIR__ . "/discovery.json";

try {
    $data = json_decode(file_get_contents("php://input"), true);
    if (!$data) exit;
    $log = json_decode(file_get_contents($file), true);

    if (isset($data['update_settings'])) {
        $log['site'] = htmlspecialchars($data['site']);
        $log['url'] = htmlspecialchars($data['url']);
        $log['whatsapp'] = htmlspecialchars($data['whatsapp']);
        $log['email'] = htmlspecialchars($data['email']);
        $log['password'] = htmlspecialchars($data['password']);
        $log['pixels'] = $data['pixels'];
        file_put_contents($file, json_encode($log, JSON_PRETTY_PRINT));
        echo json_encode(["status" => "ok"]);
        exit;
    }

    if (!isset($data["path"])) exit;
    
    // Traffic Source Logic
    if (isset($data['source'])) {
        $src = $data['source'];
        if (!isset($log['sources'])) $log['sources'] = ["YouTube" => 0, "TikTok" => 0, "Google/Ads" => 0, "Direct/Website" => 0];
        if (!isset($_SESSION['src_c'])) { $log['sources'][$src]++; $_SESSION['src_c'] = true; }
    }

    // Weekly History Rotation
    if (date('N') == 1 && $log["visitors"]["current_week_start"] !== date("Y-m-d")) {
        $log["visitors"]["week_4"] = $log["visitors"]["week_3"];
        $log["visitors"]["week_3"] = $log["visitors"]["week_2"];
        $log["visitors"]["week_2"] = $log["visitors"]["week_1"];
        $log["visitors"]["week_1"] = 0; $log["visitors"]["current_week_start"] = date("Y-m-d");
    }

    if (!isset($_SESSION['h'])) { $log["visitors"]["week_1"]++; $_SESSION['h'] = true; }

    // Engagement Scoring
    $path = filter_var($data["path"], FILTER_SANITIZE_URL);
    $found = false;
    foreach ($log["pages"] as &$p) { if ($p["url"] === $path) { $p["score"]++; $found = true; break; } }
    if (!$found) $log["pages"][] = ["url" => $path, "score" => 1];

    file_put_contents($file, json_encode($log, JSON_PRETTY_PRINT));
    echo json_encode(["status" => "ok"]);
} catch (Exception $e) { http_response_code(500); }
?>
