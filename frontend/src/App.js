import React from "react";
import ReactDOM from "react-dom";
import SentenceComponent from "./templates/SentenceComponent";
import InputField from "./templates/InputField";
import ResultComponent from "./templates/ResultComponent";

const App = () => {
  const [startTime, setStartTime] = useState(null);
  const [endTime, setEndTime] = useState(null);

  return (
    <div>
      <SentenceComponent />
      <InputField
        startTime={startTime}
        setStartTime={setStartTime}
        endTime={endTime}
        setEndTime={setEndTime}
      />
      <ResultComponent startTime={startTime} endTime={endTime} />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
