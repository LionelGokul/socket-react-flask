import React, { useEffect, useState } from "react";
import "./App.css";
import io from "socket.io-client";

// api is the namespace
let serverEndpoint = "http://127.0.0.1:5000/api";
let socket = io.connect(`${serverEndpoint}`);
socket.on("connect", function () {
  console.log(1);
});

function App() {
  const [counter, setCounter] = useState(0);

  //event for capturing data when server broadcasts msg
  socket.on("message", (msg) => {
    setCounter(msg);
  });

  useEffect(() => {}, [counter]);

  const onClick = () => {
    let count = counter + 1;
    //sending msg to the server
    //message is the event name
    //count is the data
    socket.emit("message", count);
  };

  return (
    <div className="App">
      {counter}
      <br />
      <button onClick={onClick}>Click Me!</button>
    </div>
  );
}

export default App;
