import { useState } from 'react';

function UserIcon({ user }) {
    const [isUserMenuOpen, setIsUserMenuOpen] = useState(false);


    return (

        <div>
            <div className="flex-shrink-0 flex items-center">
                <a href="/home" className="flex-shrink-0 flex items-center" >
                    <img className="block lg:hidden h-8 w-auto" src={user.urlfoto} alt="user_photo" />
                    <img className="hidden lg:block h-8 w-auto" src={user.urlfoto} alt="use_photo" />
                </a>
            </div>
        </div>




    );
}

export default UserIcon;



