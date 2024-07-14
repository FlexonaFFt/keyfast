import React from "react";

const ResultComponent = ({ startTime, endTime }) => {
  if (!startTime || !endTime) {
    return <p>Введите текст для начала тестирования</p>;
  }

  const timeTaken = (endTime - startTime) / 1000; // В секундах
  const accuracy = calculateAccuracy(); // Реализуйте функцию для расчета точности

  return (
    <div>
      <p>Время: {timeTaken} секунд</p>
      <p>Точность: {accuracy}%</p>
    </div>
  );
};

export default ResultComponent;
