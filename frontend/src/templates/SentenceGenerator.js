import React from "react";

const sentences = [
  "Быстрая коричневая лиса перепрыгивает через ленивую собаку.",
  "Музыкант играет на скрипке в оркестре.",
  "Солнце ярко светит в голубом небе.",
  // Добавьте больше предложений по своему усмотрению
];

const TextGenerator = () => {
  const getRandomSentence = () => {
    const randomIndex = Math.floor(Math.random() * sentences.length);
    return sentences[randomIndex];
  };

  return <div>{getRandomSentence()}</div>;
};

export default TextGenerator;
