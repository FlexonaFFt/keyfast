import React, { useState } from "react";
import styled from "styled-components";

const TypeInputContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
`;

const SentenceContainer = styled.div`
  font-size: 24px;
  margin-bottom: 10px;
`;

const InputContainer = styled.div`
  font-size: 24px;
`;

const TypeInput = ({ sentence }) => {
  const [typedText, setTypedText] = useState("");
  const [mistakes, setMistakes] = useState([]);

  const handleInputChange = (event) => {
    const { value } = event.target;
    const newTypedText = value;
    setTypedText(newTypedText);

    // Проверяем на ошибки
    const newMistakes = [];
    for (let i = 0; i < newTypedText.length; i++) {
      if (newTypedText[i] !== sentence[i]) {
        newMistakes.push(i);
      }
    }
    setMistakes(newMistakes);
  };

  return (
    <TypeInputContainer>
      <SentenceContainer>
        {Array.from(sentence).map((char, index) => {
          const isCorrect = typedText[index] === char;
          const isWrong = mistakes.includes(index);
          return (
            <span
              key={index}
              style={{
                color: isCorrect ? "inherit" : isWrong ? "red" : "lightgray",
              }}
            >
              {typedText[index] || char}
            </span>
          );
        })}
      </SentenceContainer>
      <InputContainer>
        <input type="text" value={typedText} onChange={handleInputChange} />
      </InputContainer>
    </TypeInputContainer>
  );
};

export default TypeInput;
