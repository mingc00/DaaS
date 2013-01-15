<!DOCTYPE html>
<html>
  <head>
    <title>DaaS</title>
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.2.2/css/bootstrap-combined.min.css" rel="stylesheet">
    <style type="text/css">
      body {
        background-color: #f5f5f5;
      }
      input[name="url"] {
        height: 35px;
        width: 70%;
        font-size: large;
        margin-right: 10px;
      }

      h1 {
        padding-bottom: 50px;
      }

      .box {
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        padding: 20px 0px 20px 0px;
        background-color: #fff;
        border: 1px solid #e5e5e5;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        -webkit-box-shadow: 0 1px 2px rgba(0,0,0,.05);
        -moz-box-shadow: 0 1px 2px rgba(0,0,0,.05);
        box-shadow: 0 1px 2px rgba(0,0,0,.05);
      }

      #bar {
        margin-top: 100px;
      }

      #download_list {
        margin-top: 50px;
      }

      #download_list table {
        width: 70%;
        margin: 10px auto 10px auto;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div id="bar" class="box">
        <h1>Download as a Service</h1>
        <form method="post" action="/search" class="form-search">
          <input name="url" type="text" class="input-xxlarge"
            placeholder="What do you want to download?"/>
          <button type="submit" class="btn btn-primary btn-large">Download</button>
        </form>
      </div>
    %if results:
      <div class="box" id="download_list">
        <table class="table">
          <tr><th>URL</th><th>Status</th></tr>
        %for item in results:
          <tr>
            <td>{{item['url']}}</td>
            <td>{{item['status']}}</td>
          </tr>
        </table>
      </div>
    %end
    </div>
  </body>
</html>