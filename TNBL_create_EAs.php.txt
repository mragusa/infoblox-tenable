<?php
  $NIOS_baseURL="https://127.0.0.1/wapi/v2.6/";
  $NIOS_User="admin";
  $NIOS_PWD="infoblox";


  #extensibleattributedef

  $ch = curl_init();
  curl_setopt_array($ch,array(
    CURLOPT_USERPWD => $NIOS_User . ":" . $NIOS_PWD,
    CURLOPT_CUSTOMREQUEST => "POST",
    CURLOPT_SSL_VERIFYPEER => false,
#    CURLOPT_VERBOSE => true,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => array('Content-Type: application/json')
    )
  );

  $data=[
         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_Sync", comment=>"Sync the object", type=>"ENUM", flags=>"I", default_value=>"true", list_values=>[[value=>"true"],[value=>"false"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_SyncTime", comment=>"Sync Date/Time", type=>"STRING"]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AddNet", comment=>"Add a network to Tenable", type=>"ENUM", flags=>"I", default_value=>"true", list_values=>[[value=>"true"],[value=>"false"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AddRange", comment=>"Add a range to Tenable", type=>"ENUM", flags=>"I", default_value=>"true", list_values=>[[value=>"true"],[value=>"false"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_ScanOnEvnt", comment=>"Scan an asset by an event", type=>"ENUM", flags=>"I", default_value=>"true", list_values=>[[value=>"true"],[value=>"false"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_ScanOnAdd", comment=>"Scan an asset after provisioning", type=>"ENUM", flags=>"I", default_value=>"true", list_values=>[[value=>"true"],[value=>"false"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_ScanTemplate", comment=>"Scan template", type=>"ENUM", flags=>"I", default_value=>"IB Scan", list_values=>[[value=>"IB Scan"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_ScanTemplateID", comment=>"Scan ID. Updated automatically", type=>"INTEGER", default_value=>"0", flags=>"I"]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AssetIP", comment=>"Assets Fixed IP", type=>"ENUM", flags=>"I", default_value=>"IB Static", list_values=>[[value=>"IB Static"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AssetIPID", comment=>"ID Assets Fixed IP. Updated automatically", type=>"INTEGER", default_value=>"0", flags=>"I"]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AssetHost", comment=>"Assets Fixed Hostnames", type=>"ENUM", flags=>"I", default_value=>"IB Static DNS", list_values=>[[value=>"IB Static DNS"]]]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AssetHostID", comment=>"ID Assets Fixed Hostnames. Updated automatically", type=>"INTEGER", default_value=>"0", flags=>"I"]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_ScanTime", comment=>"Last Scan Date. Updated automatically", type=>"STRING", default_value=>"0"]],

         [call=>"extensibleattributedef",
         data=>[name=>"TNBL_AddByHostname", comment=>"Add a host by a hostname", type=>"ENUM", flags=>"I", default_value=>"true", list_values=>[[value=>"true"],[value=>"false"]]]],


  ];

  foreach ($data as $api_call){
    $data_string = json_encode($api_call{data});
    curl_setopt($ch, CURLOPT_URL, $NIOS_baseURL.$api_call{call});
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);

    $result = curl_exec($ch);
  #  print_r($result);
    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $res=json_decode($result);
    print_r($res);
  };

  curl_close($ch);

?>
