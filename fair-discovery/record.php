<?php
header("Content-Type: application/json");
session_start();

$file = __DIR__ . "/discovery.json";

try {
    $data = json_decode(file_get_contents("php://input"), true);
    if (!$data) exit;

    $log = json_decode(file_get_contents($file), true);

    // --- HANDLE SETTINGS UPDATE ---
    if (isset($data['update_settings'])) {
        $log['site'] = filter_var($data['site'], FILTER_SANITIZE_STRING);
        $log['whatsapp'] = filter_var($data['whatsapp'], FILTER_SANITIZE_STRING);
        $log['email'] = filter_var($data['email'], FILTER_SANITIZE_EMAIL);
        $log['password'] = filter_var($data['password'], FILTER_SANITIZE_STRING);
        file_put_contents($file, json_encode($log, JSON_PRETTY_PRINT));
        echo json_encode(["status" => "updated"]);
        exit;
    }

    // --- NORMAL DATA RECORDING ---
    // Bot Check: Ignore if no score and no path
    if (!isset($data["path"]) || (int)$data["score"] === 0) exit;

    // Weekly Reset (Mondays)
    if (date('N') == 1 && $log["visitors"]["current_week_start"] !== date("Y-m-d")) {
        $log["visitors"]["week_4"] = $log["visitors"]["week_3"];
        $log["visitors"]["week_3"] = $log["visitors"]["week_2"];
        $log["visitors"]["week_2"] = $log["visitors"]["week_1"];
        $log["visitors"]["week_1"] = 0;
        $log["visitors"]["current_week_start"] = date("Y-m-d");
    }

    // Unique Human Visitor Count
    if (!isset($_SESSION['counted'])) {
        $log["visitors"]["week_1"]++;
        $_SESSION['counted'] = true;
    }

    // Page Score
    $path = filter_var($data["path"], FILTER_SANITIZE_URL);
    $found = false;
    foreach ($log["pages"] as &$p) {
        if ($p["url"] === $path) { $p["score"] += (int)$data["score"]; $found = true; break; }
    }
    if (!$found) $log["pages"][] = ["url" => $path, "score" => (int)$data["score"]];

    file_put_contents($file, json_encode($log, JSON_PRETTY_PRINT));
    echo json_encode(["status" => "ok"]);

} catch (Exception $e) { http_response_code(500); }
?>
