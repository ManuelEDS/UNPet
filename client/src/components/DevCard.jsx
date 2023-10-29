

import { Card, CardContent, Typography, CardMedia, Box } from '@mui/material';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';
import GitHubIcon from '@mui/icons-material/GitHub';

const DevCard = ({ name, skills, photo, fb = '#', twt = '#', inst = '#', gh='#' }) => {
   // console.log('devacrd: '+name+' skills: '+skills+' photo: '+photo+' fb: '+fb+' twt: '+twt+' inst: '+inst+' gh: '+gh);
    return (
        <Card sx={{ maxHeight: 'auto', maxWidth: 300, borderRadius: 5 }}>
            <CardMedia
                component="img"
                image={photo}
                alt={name}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                    {name}
                </Typography>
                <Typography gutterBottom variant="body2" color="textSecondary" component="p" sx={{ marginBottom: 3 }}>
                    {skills}
                </Typography>
                <div style={{ display: 'flex', justifyContent: 'center' }}>
                    <a href="https://www.facebook.com/" target="_blank" rel="noopener" style={{ margin: 'auto' }}>
                        <FacebookIcon color="primary" />
                    </a>
                    <a href="https://twitter.com/" target="_blank" rel="noopener" style={{ margin: 'auto' }}>
                        <TwitterIcon color="primary" />
                    </a>
                    <a href="https://www.instagram.com/" target="_blank" rel="noopener" style={{ margin: 'auto' }}>
                        <InstagramIcon color="primary" />
                    </a>
                    <a href="https://www.github.com/" target="_blank" rel="noopener" style={{ margin: 'auto' }}>
                        <GitHubIcon color="primary" />
                    </a>
                </div>
            </CardContent>
        </Card>
    );
};

export default DevCard;
