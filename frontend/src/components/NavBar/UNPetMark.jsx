import { useContext } from "react";
import { UserContext } from "../../context/UserContext";
import { useMediaQuery } from 'react-responsive';

function UNPetMark({logo}) {
    const isDesktopOrLaptop = useMediaQuery({ minDeviceWidth: 800 });

    const {user} = useContext(UserContext);
    return (
        <>
            <div >
                <div className="flex-shrink-0 flex items-center">
                    <a href="/home" className={`flex-shrink-0 flex items-center ${user.isDesktopOrLaptop && 'ml-3'}`} >
                        <img className=" h-8 w-auto" src={logo} alt="UNPet logo" />
                        
                        {user.isDesktopOrLaptop && <h1 className="text-white font-bold ml-2">UNPet</h1>}
                    </a>
                </div>

            </div>
        </>
    );
}

export default UNPetMark;
