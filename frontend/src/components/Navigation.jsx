import { Card, CardContent, Typography, CardMedia, makeStyles, List, ListItemButton, ListItemIcon, ListItemText } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';
import HomeIcon from '@material-ui/icons/Home';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import RecentActorsIcon from '@mui/icons-material/RecentActors';
import PetsIcon from '@mui/icons-material/Pets';
import AddCircleIcon from '@mui/icons-material/AddCircle';

const useStyles = makeStyles((theme) => ({
  sidebar: {
    position: 'fixed',
    height: '100%',
    width: '200px',
    backgroundColor: '#f5f5f5',
    padding: '1rem',
    [theme.breakpoints.down('sm')]: {
      position: 'static',
      width: '100%',
    },
  },
}));

export function Navigation() {
  const classes = useStyles();

  return (
    <div className={classes.sidebar}>
      <List>
        <ListItemButton component={RouterLink} to="/">
          <ListItemIcon>
            <HomeIcon />
          </ListItemIcon>
          <ListItemText primary="Inicio" />
        </ListItemButton>
        <ListItemButton component={RouterLink} to="/trending">
          <ListItemIcon>
            <TrendingUpIcon />
          </ListItemIcon>
          <ListItemText primary="Tendencias" />
        </ListItemButton>
        <ListItemButton component={RouterLink} to="/recent">
          <ListItemIcon>
            <RecentActorsIcon />
          </ListItemIcon>
          <ListItemText primary="Recientes" />
        </ListItemButton>
        <ListItemButton component={RouterLink} to="/pets">
          <ListItemIcon>
            <PetsIcon />
          </ListItemIcon>
          <ListItemText primary="Mascotas" />
        </ListItemButton>
        <ListItemButton component={RouterLink} to="/pet-create">
          <ListItemIcon>
            <AddCircleIcon />
          </ListItemIcon>
          <ListItemText primary="Crear Mascota" />
        </ListItemButton>
      </List>
    </div>
  );
}