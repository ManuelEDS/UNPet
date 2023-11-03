import { Fragment } from 'react';
import { FaHeart } from 'react-icons/fa';
import DevCard from '../components/DevCard';

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
]


export const HomePage = () => {
    posts.map((post) => console.log(post.id));

    return (
        <div className="max-w-sm mx-auto">
            <h2 className="text-3xl font-bold text-center mb-4">Bienvenido a UNPet!</h2>
            <p className="text-center mb-8">Donando nuevas oportunidades</p>
            {posts.map((post) => (
                <div key={post.id} className="bg-white rounded-lg shadow-lg mb-8">
                    <div className="p-4">
                        <div className="flex items-center mb-4">
                            <img src={post.authorImg} alt={post.author} className="w-10 h-10 rounded-full mr-2" />
                            <p className="text-sm font-medium">{post.author}</p>
                        </div>
                        <h3 className="text-lg font-medium mb-2">{post.title}</h3>
                        <p className="text-gray-500 text-sm mb-4">{post.content}</p>
                        <div className="flex items-center justify-between">
                            <p className="text-gray-500 text-sm">{post.date}</p>
                            <div className="flex items-center">
                                <FaHeart className="w-5 h-5 text-red-500 mr-1" />
                                <p className="text-gray-500 text-sm">{post.likes}</p>
                            </div>
                        </div>
                    </div>
                </div>
            ))}
            <DevCard
                name={'Cesar rincon robayo rr desarrollo sociocultural'}
                skills={
                    'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'
                }
                photo={posts[0].authorImg}
                fb={'facebook.com'}
                twt={'twitter.com'}
                inst={'instagram.com'}
            />
            <div className="grid grid-cols-3 gap-4">
                <DevCard
                    name={'Cesar rincon robayo rr desarrollo sociocultural'}
                    skills={
                        'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'
                    }
                    photo={posts[0].authorImg}
                    fb={'facebook.com'}
                    twt={'twitter.com'}
                    inst={'instagram.com'}
                    gh="github.com"
                />
                <DevCard
                    name={'Cesar rincon robayo rr desarrollo sociocultural'}
                    skills={
                        'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'
                    }
                    photo={posts[0].authorImg}
                    fb={'facebook.com'}
                    twt={'twitter.com'}
                    inst={'instagram.com'}
                    gh="github.com"
                />
                <DevCard
                    name={'Cesar rincon robayo rr desarrollo sociocultural'}
                    skills={
                        'Programador backend, Lorem ipsum dolor sit amet conse deserunt suscipit qui nisi architecto dolores, esse ratione voluptates omnis facere incidunt culpa.'
                    }
                    photo={posts[0].authorImg}
                    fb={'facebook.com'}
                    twt={'twitter.com'}
                    inst={'instagram.com'}
                    gh="github.com"
                />
            </div>
        </div>
    );
};

export default HomePage;





// {
//     id: 2,
//     title: 'Mi segundo post',
//     content: 'Este es mi segundo post en UNPet!',
//     author: 'Maria Rodriguez',
//     date: '2021-10-02',
//     likes: 5,
//     authorImg: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Maria%20Rodriguez'
// },
// {
//     id: 3,
//     title: 'Mi tercer post',
//     content: 'Este es mi tercer post en UNPet!',
//     author: 'Pedro Gomez',
//     date: '2021-10-03',
//     likes: 2,
//     authorImg: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Pedro%20Gomez'
// }
// ];
