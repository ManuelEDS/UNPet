import { useState } from 'react';

export function FAQ() {
  const [showAnswers, setShowAnswers] = useState([]);

  const toggleAnswer = (index) => {
    setShowAnswers((prevAnswers) => {
      const newAnswers = [...prevAnswers];
      newAnswers[index] = !newAnswers[index];
      return newAnswers;
    });
  };

  const FAQList = [
    {
      question: '¿Cómo funciona UNPet?',
      answer: 'UNPet es una página web que conecta refugios con personas que quieran adoptar mascotas. Los refugios publican información sobre las mascotas disponibles para adopción y los posibles adoptantes pueden contactarlos a través de la página para iniciar el proceso de adopción.'
    },
    {
      question: '¿Quiénes pueden publicar mascotas para adopción en UNPet?',
      answer: 'Solo los refugios pueden publicar mascotas para su adopción en UNPet.'
    },
    {
      question: '¿Cómo puedo adoptar una mascota a través de UNPet?',
      answer: 'Para adoptar una mascota a través de UNPet, debes buscar en la página las mascotas disponibles para adopción y contactar al refugio que publicó la información. El refugio te proporcionará más información sobre la mascota y el proceso de adopción.'
    },
    {
      question: '¿Qué información necesito proporcionar para adoptar una mascota?',
      answer: 'El refugio te pedirá información básica sobre ti y tu hogar para asegurarse de que la mascota se adapte bien a su nuevo hogar. Esto puede incluir información sobre tu hogar, tu estilo de vida y tu experiencia previa con mascotas.'
    },
    {
      question: '¿Cómo puedo asegurarme de que estoy adoptando una mascota responsablemente?',
      answer: 'UNPet promueve la adopción responsable y recomienda que los posibles adoptantes se informen sobre las necesidades de la mascota antes de adoptarla. Además, UNPet ha implementado un chat entre el adoptante y el refugio para que se pueda llevar un seguimiento de una adopción responsable.'
    },
    {
      question: '¿Cómo puedo encontrar refugios cercanos a mi ubicación?',
      answer: 'En la página de inicio de UNPet, puedes buscar refugios cercanos a tu ubicación ingresando tu código postal o ciudad en la barra de búsqueda.'
    },
    {
      question: '¿Puedo adoptar una mascota si vivo en un apartamento?',
      answer: 'Sí, puedes adoptar una mascota si vives en un apartamento. Sin embargo, debes asegurarte de que la mascota se adapte bien a un espacio más pequeño y que puedas proporcionarle suficiente ejercicio y estimulación mental.'
    },
    {
      question: '¿Cómo puedo apoyar a UNPet si no puedo adoptar una mascota?',
      answer: 'Puedes apoyar a UNPet compartiendo información sobre la página en tus redes sociales o haciendo una donación para ayudar a cubrir los costos de mantenimiento de la página.'
    },
    {
      question: '¿Qué pasa si la mascota que adopté no se adapta bien a mi hogar?',
      answer: 'Si la mascota que adoptaste no se adapta bien a tu hogar, debes contactar al refugio para informarles de la situación. El refugio puede ayudarte a encontrar una solución, como proporcionarte recursos para ayudar a la mascota a adaptarse o aceptar la devolución de la mascota.'
    }
  ];

  return (
    <div className="w-full max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold text-center mb-4 mt-10">Preguntas Frecuentes</h1>
      <ul className='mb-20'>
        {FAQList.map((faq, index) => (
            <li key={index} className='mb-6 rounded-md' style={{ backgroundColor: 'white' }}>
            <div className="border rounded-md py-6">
              <button
                className="px-4 py-2 text-gray-700 font-bold h-full w-full text-center rounded-md"
                onClick={() => toggleAnswer(index)}
              >
                {faq.question}
              </button>
              {showAnswers[index] && (
                <div className="px-4 py-2 text-gray-700 mt-2 text-center">
                  {faq.answer}
                </div>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

