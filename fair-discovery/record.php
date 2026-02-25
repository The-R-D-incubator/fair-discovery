<?php
header("Content-Type: application/json");
session_start();

try {
    $input = file_get_contents("php://input");
    $data = json_decode($input, true);
    
    if (!$data || !isset($data["path"])) {
        http_response_code(400);
        exit;
    }

    $file = __DIR__ . "/discovery.json";
    $fp = fopen($file, 'c+');
    if (!flock($fp, LOCK_EX)) throw new Exception("Lock Fail");

    $fileSize = filesize($file);
    $jsonContent = $fileSize > 0 ? fread($fp, $fileSize) : "{}";
    $log = json_decode($jsonContent, true);

    // Weekly Rotation Logic 
    $isMonday = (date('N') == 1);
    if ($isMonday && $log["visitors"]["current_week_start"] !== date("Y-m-d")) {
        $log["visitors"]["week_4"] = $log["visitors"]["week_3"];
        $log["visitors"]["week_3"] = $log["visitors"]["week_2"];
        $log["visitors"]["week_2"] = $log["visitors"]["week_1"];
        $log["visitors"]["week_1"] = 0;
        $log["visitors"]["current_week_start"] = date("Y-m-d");
    }

    // Unique Human Visitor Count [cite: 8]
    if (!isset($_SESSION['counted_visitor']) && (int)$data["score"] > 0) {
        $log["visitors"]["week_1"]++;
        $_SESSION['counted_visitor'] = true;
    }

    // Update Page Score
    $path = filter_var($data["path"], FILTER_SANITIZE_URL);
    $found = false;
    foreach ($log["pages"] as &$p) {
        if ($p["url"] === $path) { $p["score"] += (int)$data["score"]; $found = true; break; }
    }
    if (!$found) $log["pages"][] = ["url" => $path, "score" => (int)$data["score"]];

    ftruncate($fp, 0);
    rewind($fp);
    fwrite($fp, json_encode($log, JSON_PRETTY_PRINT));
    flock($fp, LOCK_UN);
    fclose($fp);
    echo json_encode(["status" => "ok"]);

} catch (Exception $e) { http_response_code(500); }
?>
