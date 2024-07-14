import React, { useState } from "react";

const InputField = () => {
  const [inputValue, setInputValue] = useState("");
  const [startTime, setStartTime] = useState(null);
  const [endTime, setEndTime] = useState(null);
  const [correctLetters, setCorrectLetters] = useState({});

  const handleInputChange = (event) => {
    const userInput = event.target.value;
    setInputValue(userInput);

    // Запуск таймера при начале ввода
    if (!startTime && userInput.length > 0) {
      setStartTime(new Date().getTime());
    }
  };

  const handleInputBlur = () => {
    // Остановка таймера при завершении ввода
    if (startTime && !endTime) {
      setEndTime(new Date().getTime());
    }

    const userInput = event.target.value;
    const sentence = "This is a sample sentence.";
    const userInputArray = userInput.split("");
    const sentenceArray = sentence.split("");

    userInputArray.forEach((letter, index) => {
      if (letter === sentenceArray[index]) {
        setCorrectLetters((prevCorrectLetters) => ({
          ...prevCorrectLetters,
          [index]: true,
        }));
      } else {
        setCorrectLetters((prevCorrectLetters) => ({
          ...prevCorrectLetters,
          [index]: false,
        }));
      }
    });
  };

  return (
    <input
      type="text"
      value={inputValue}
      onChange={handleInputChange}
      onBlur={handleInputBlur}
    />
  );
};

export default InputField;
