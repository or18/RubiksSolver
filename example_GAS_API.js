function callAPI() {
  var url = "https://b9a44f7f2c7889ff26.gradio.live/call/run_solver/";
  var payload = {
    data: ["F2L_solver",
      "B' D L2 U F2 L2 U' B2 F2 D2 R2 B2 F R2 U2 R U2 B D L2 R'",
      "z2",
      "False",
      "False",
      "False",
      "False",
      7,
      "UDLRFB"
    ]
  }
  var options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };
  try {
    var response = UrlFetchApp.fetch(url, options);
    var jsonResponse = JSON.parse(response.getContentText());
    var eventId = jsonResponse["event_id"]
    var options = {
      method: "get",
      muteHttpExceptions: true
    };
    var response = UrlFetchApp.fetch(url+eventId, options);
    var result = response.getContentText()
    Logger.log(result);
  } catch (e) {
    Logger.log(e);
  }
}
