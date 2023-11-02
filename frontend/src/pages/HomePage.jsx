import React from 'react';
//import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Card, CardContent, Link, Typography } from '@mui/material';
import DevCard from '../components/DevCard';
import Box from '@mui/material/Box';
import NavBar from '../components/NavBar/NavBar';
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
    posts.map((post) => (console.log(post.id)));

    return (
        <Container maxWidth="sm">
            <Typography variant="h2" align="center" gutterBottom>
                Bienvenido a UNPet!
            </Typography>
            <Typography variant="body1" align="center" paragraph>
                Donando nuevas oportunidades
            </Typography>
            {posts.map((post) => (

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
                        </div>Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.
                    </CardContent>
                </Card>
            ))}
            <DevCard name={'Cesar rincon robayo rr desarrollo sociocultural'} skills={'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'} photo={posts[0].authorImg} fb={'facebook.com'} twt={'twitter.com'} inst={'instagram.com'}></DevCard>
            <Container maxWidth="sm">
            
                <Box style={{ position: 'relative' }}>
                    <DevCard name={'Cesar rincon robayo rr desarrollo sociocultural'} skills={'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'} photo={posts[0].authorImg} fb={'facebook.com'} twt={'twitter.com'} inst={'instagram.com'} gh='github.com'  />
                </Box>
                <Box style={{ position: 'relative' }}>
                    <DevCard name={'Cesar rincon robayo rr desarrollo sociocultural'} skills={'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'} photo={posts[0].authorImg} fb={'facebook.com'} twt={'twitter.com'} inst={'instagram.com'} gh='github.com'  />
                </Box>
                <Box style={{ position: 'relative' }}>
                    <DevCard name={'Cesar rincon robayo rr desarrollo sociocultural'} skills={'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'} photo={posts[0].authorImg} fb={'facebook.com'} twt={'twitter.com'} inst={'instagram.com'} gh='github.com'  />
                </Box>
            </Container>
            {/* <NavBar></NavBar> */}
        </Container>
    );
};

export default HomePage;
