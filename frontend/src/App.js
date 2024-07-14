import "./styles/main.css";
import "./App.css";
import TypeSpeedTest from "./templates/TypeSpeedTest.js";
import SentenceGenerator from "./templates/SentenceGenerator.js";

function App() {
  const sentence = SentenceGenerator();

  return (
    <header className="main">
      <div>
        <SentenceGenerator />
        <TypeSpeedTest sentence={sentence} />
      </div>
    </header>
  );
}

export default App;
