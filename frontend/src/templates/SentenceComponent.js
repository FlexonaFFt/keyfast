import React from "react";

const SentenceComponent = () => {
  const sentence = "This is a sample sentence.";
  const correctLetters = {}; // Получите correctLetters из InputField

  return (
    <div>
      {sentence.split("").map((letter, index) => (
        <span
          key={index}
          style={{
            color: correctLetters[index] ? "white" : "red",
          }}
        >
          {letter}
        </span>
      ))}
    </div>
  );
};

export default SentenceComponent;
