import React from 'react';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';
import { Card, CardContent, Link, Typography } from '@mui/material';
import Markdown from 'react-markdown';
import {GetMDText} from '../components/DmText';

export function Legal({ title, description, imageUrl, descriptionMd }) {
    
    return (
        <Card sx={{ maxWidth: 900, margin: 'auto', marginTop: 4 }}>
            <CardContent sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <Typography variant="h4" gutterBottom >
                    {title}
                </Typography>
                <Typography variant="body1" gutterBottom sx={{ whiteSpace: 'pre-wrap' , margin:4}}>
                    {descriptionMd !=''? (
                        <Markdown>{GetMDText(descriptionMd)}</Markdown>
                    ) : (
                        <span>{description}</span>
                    )}
                </Typography>
                {imageUrl && (
                    <img src={imageUrl} alt="Legal Info" style={{ maxWidth: '200px', marginTop: 2 }} />
                )}
                <div sx={{ display: 'flex', justifyContent: 'center', marginTop: 2 }}>
                    <Link href="https://www.facebook.com/" target="_blank" rel="noopener" sx={{ margin: 'auto' }}>
                        <FacebookIcon />
                    </Link>
                    <Link href="https://twitter.com/" target="_blank" rel="noopener" sx={{ margin: 'auto' }}>
                        <TwitterIcon />
                    </Link>
                    <Link href="https://www.instagram.com/" target="_blank" rel="noopener" sx={{ margin: 'auto' }}>
                        <InstagramIcon />
                    </Link>
                </div>
                <Typography variant="body2" color="textSecondary" align="center" sx={{ marginTop: 2 }}>
                    © {new Date().getFullYear()} UNPet. Todos los derechos reservados.
                </Typography>
            </CardContent>
        </Card>
    );
}





