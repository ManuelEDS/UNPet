// PostCard.jsx
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Card, CardContent, Typography, CardMedia, styled } from '@mui/material';

const useStyles = styled({
  card: {
    width: '100%',
  },
  media: {
    height: 0,
    paddingTop: '56.25%', // 16:9
  },
});




export const PostCard = ({ post }) => {
  const classes = useStyles();
  const { fotos, titulo, estado, descripcion, fechaPublicacion, likes } = post;

  // Formatear la fecha
  const fecha = new Date(fechaPublicacion).toLocaleDateString();

  return (
    <Card className={classes.card}>
      {/* Mostrar la primera foto */}
      {fotos[0] && <CardMedia className={classes.media} image={fotos[0]} />}

      <CardContent>
        <Typography variant="h5">{titulo}</Typography>
        <Typography variant="subtitle1">{estado}</Typography>
        <Typography variant="body2">{descripcion}</Typography>
        <Typography variant="caption">{fecha}</Typography>
        <Typography variant="caption">
          <FavoriteIcon /> {likes}
        </Typography>
      </CardContent>

      {/* Mostrar las demás fotos */}
      {fotos.slice(1).map((foto, index) => (
        <CardMedia key={index} className={classes.media} image={foto} />
      ))}
    </Card>
  );
};



const post = {
    fotos: ['https://dummyimage.com/600x500&text=mascota+foto', 'https://dummyimage.com/600x500&text=mascota+foto'],
    titulo: 'Mi primer post',
    estado: 'publicado',
    descripcion: 'Este es el contenido de mi primer post.',
    fechaPublicacion: "2023-09-30T14:30:00Z",
    likes: 100
  };