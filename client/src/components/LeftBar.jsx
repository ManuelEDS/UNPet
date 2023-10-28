import React from 'react';
import { Avatar } from '@mui/material/Avatar'

function LeftBar() {
    return (
        <div className="left-bar">
            <ul>
                <li>Home</li>
                <li>Trends</li>
                <li>Favorites</li>
                <li>Config</li>
            </ul>
            <div className="user-section">
                <Avatar alt="User Profile" src="/static/images/avatar/1.jpg" />
                <span>User Name</span>
            </div>
        </div>
    );
}

export default LeftBar;
