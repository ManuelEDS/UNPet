import HeroSlider, { Slide, MenuNav } from "hero-slider";
import { useState } from 'react';

// Asumiendo que tienes un array de mascotas con una propiedad 'image' que contiene la URL de la imagen


// eslint-disable-next-line react/prop-types
function ImageSlider({ images, currentSlide, setCurrentSlide }) {
    const [slide, setSlide] = useState(currentSlide || 0);

    const handleBeforeSliding = (previousSlide, nextSlide) => {
        console.debug(
            "onBeforeSliding(previousSlide, nextSlide): ",
            previousSlide,
            nextSlide
        );
        setSlide(nextSlide);
        if (setCurrentSlide) {
            setCurrentSlide(nextSlide);
        }
    };

    const handleAfterSliding = (nextSlide) => {
        console.debug("onAfterSliding(nextSlide): ", nextSlide);
        setSlide(nextSlide);
        if (setCurrentSlide) {
            setCurrentSlide(nextSlide);
        }
    };

    return (
        <HeroSlider
            height={"100vh"}
            autoplay
            controller={{
                initialSlide: slide,
                slidingDuration: 500,
                slidingDelay: 100,
                onSliding: (nextSlide) =>
                    console.debug("onSliding(nextSlide): ", nextSlide),
                onBeforeSliding: handleBeforeSliding,
                onAfterSliding: handleAfterSliding
            }}
        >
            {images.map((item, index) => (
                <Slide
                    key={index}
                    background={{
                        backgroundImageSrc: item.urlfoto
                    }}
                />
            ))}
            <MenuNav />
        </HeroSlider>
    );
}

export default ImageSlider;
    

