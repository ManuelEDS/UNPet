// PostCard.jsx
import { Card, CardContent, IconButton } from '@material-ui/core';
import FavoriteIcon from '@material-ui/icons/Favorite';

export const PostCard = ({ post }) => (
  <Card>
    <CardContent>
      {/* Aquí va el contenido del post */}
      <IconButton>
        <FavoriteIcon />
      </IconButton>
      {/* Aquí van los demás elementos del post */}
    </CardContent>
  </Card>
);


// CardContainer.jsx
// CardContainer.jsx
import { styled } from '@material-ui/core/styles';

const useStyles = styled({
  container: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
  },
});

export const CardContainer = ({ children }) => {
  const classes = useStyles();

  return (
    <div className={classes.container}>
      {/* Aquí se renderizan las cards */}
      {children}
    </div>
  );
};