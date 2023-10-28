import React from 'react';
//import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Card, CardContent, Link, Typography } from '@mui/material';
const posts = [
    {
        id: 1,
        title: 'Mi primer post',
        content: 'Este es mi primer post en UNPet!',
        author: 'Juan Perez',
        date: '2021-10-01',
        likes: 10,
        authorImg: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Juan%20Perez'
    },
    {
        id: 2,
        title: 'Mi segundo post',
        content: 'Este es mi segundo post en UNPet!',
        author: 'Maria Rodriguez',
        date: '2021-10-02',
        likes: 5,
        authorImg: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Maria%20Rodriguez'
    },
    {
        id: 3,
        title: 'Mi tercer post',
        content: 'Este es mi tercer post en UNPet!',
        author: 'Pedro Gomez',
        date: '2021-10-03',
        likes: 2,
        authorImg: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Pedro%20Gomez'
    }
];


export const HomePage = () => {
    return (
        <Container maxWidth="sm">
            <Typography variant="h2" align="center" gutterBottom>
                Bienvenido a UNPet!
            </Typography>
            <Typography variant="body1" align="center" paragraph>
                Donando nuevas oportunidades
            </Typography>
            {posts.map(post => (
                <>
                <Card key={post.id} className="post-container">
                    <CardContent>
                        <div className="post-header">
                        <Container maxWidth="sm">
                        <img src={post.authorImg} alt={post.author} className="author-img" />
                        </Container>
                            
                            <Typography variant="subtitle1" gutterBottom>
                                {post.author}
                            </Typography>
                        </div>
                        <div className="post-body">
                            <Typography variant="h5" gutterBottom>
                                {post.title}
                            </Typography>
                            <Typography variant="body1" gutterBottom>
                                {post.content}
                            </Typography>
                        </div>
                        <div className="post-footer">
                            <Typography variant="subtitle1" gutterBottom>
                                {post.date}
                            </Typography>
                            <div className="likes-container">
                                <FavoriteIcon className="like-icon" />
                                <Typography variant="subtitle1" gutterBottom>
                                    {post.likes}
                                </Typography>
                            </div>
                        </div>
                    </CardContent>
                </Card>
                <br />
                </>
            ))}
        </Container>
    );
};

export default HomePage;
