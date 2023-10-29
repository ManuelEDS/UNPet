import { Card, CardContent, CardMedia, Typography } from '@mui/material';

const cards = [
    {
        id: 1,
        title: 'Card 1',
        description: 'This is the description for card 1',
        image: 'https://source.unsplash.com/random/300x200',
    },
    {
        id: 2,
        title: 'Card 2',
        description: 'This is the description for card 2',
        image: 'https://source.unsplash.com/random/300x200',
    },
    {
        id: 3,
        title: 'Card 3',
        description: 'This is the description for card 3',
        image: 'https://source.unsplash.com/random/300x200',
    },
];

const Ex1 = () => {
    return (
        <div style={{ display: 'flex', flexDirection: 'row', flexWrap: 'wrap' }}>
            {cards.map((card) => (
                <Card key={card.id} sx={{ maxWidth: 345, margin: '0.5rem', width: '100%', '@media (min-width: 600px)': { width: 'calc(33.33% - 1rem)' }, '@media (max-width: 600px)': { flexDirection: 'column' } }}>
                    <CardMedia
                        component="img"
                        height="140"
                        image={card.image}
                        alt={card.title}
                    />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="div">
                            {card.title}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                            {card.description}
                        </Typography>
                    </CardContent>
                </Card>
            ))}
        </div>
    );
};

export default Ex1;
