import HeroSlider, { Slide, MenuNav } from "hero-slider";
import { useState } from 'react';

// Asumiendo que tienes un array de mascotas con una propiedad 'image' que contiene la URL de la imagen


// eslint-disable-next-line react/prop-types
function ImageSlider({ images, currentSlide, setCurrentSlide }) {
    const [slide, setSlide] = useState(currentSlide || 0);
    console.log('images', images);
    const length = images.length;
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
        <>
            {length > 1 ?
            <HeroSlider
                height={"100vh"}
                autoplay

                controller={{
                    initialSlide: slide,
                    onSliding: (nextSlide) =>
                        console.debug("onSliding(nextSlide): ", nextSlide),
                    onBeforeSliding: handleBeforeSliding,
                    onAfterSliding: handleAfterSliding
                }}
                style={{ maxHeight: '600px' }}
            >
                {images.map((item, index) => (
                    <a href="#"><Slide
                    key={index}
                    background={{
                        backgroundImageSrc: item.urlfoto
                    }}
                /></a>
                    
                ))}

                <MenuNav />
            </HeroSlider>:
            <a href="#">
                 <img src={images[0].urlfoto} alt="" />
            </a>
          
            }

        </>
    );
}

export default ImageSlider;


