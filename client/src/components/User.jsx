import React from 'react';
import { Card, CardContent, Typography } from '@mui/material/';

const User = ({ user }) => {
    console.log(user, user.username);
    return (
        <Card>
            <CardContent>
                <Typography variant="h5" component="h2">
                    {user.username}
                </Typography>
                <Typography color="textSecondary">
                    {user.email}
                </Typography>
                <Typography color="textSecondary">
                    {user.localidad}
                </Typography>
                <Typography variant="body2" component="p">
                    <a href={user.urlfoto}></a>
                </Typography>
            </CardContent>
        </Card>
    );
};

export default User;
