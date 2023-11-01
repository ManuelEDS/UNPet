import React from 'react';
import FacebookIcon from '@mui/icons-material/Facebook';
import TwitterIcon from '@mui/icons-material/Twitter';
import InstagramIcon from '@mui/icons-material/Instagram';
import { Card, CardContent, Typography } from '@mui/material';
import Markdown from 'react-markdown';
import { GetMDText } from '../components/DmText';
import { Link } from 'react-router-dom'

export function Legal({ title, description = 'Inserte descripción aqui', imageUrl, descriptionMd = '', listUrls }) {
    console.log('url md desde legal:' + descriptionMd);
    return (
        <Card sx={{ maxWidth: 900, margin: 'auto', marginTop: 4 }}>
            <CardContent sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: 5 }}>
                <Typography variant="h4" gutterBottom >
                    {title}
                </Typography>
                {<div sx={{ display: 'flex', justifyContent: 'center', marginTop: 2 }}>
                    {descriptionMd != '' ? (

                        <Markdown >{GetMDText(descriptionMd)}</Markdown>
                    ) : (
                        <span>{description}</span>
                    )}
                </div>}
                <div>
                    {listUrls && (<>
                        <Typography variant="h6" gutterBottom sx={{ textAlign: 'center' }}>
                            También puedes ver
                        </Typography>
                        {listUrls.map((item, index) => (
                            <div key={index}>
                                <Typography variant="body2" gutterBottom sx={{ textAlign: 'center' }}>
                            <Link to={item.url}  sx={{ mt: 4, mb: 2, fontSize: 24, textAlign: 'center' }}>
                                {item.name}
                            </Link>
                            </Typography>
                            </div>
                            
                            
                        ))}
                    </>
                    )}
                    {!listUrls && <p>No hay elementos</p>}
                </div>
                {imageUrl && (
                    <img src={imageUrl} alt="Legal Info" style={{ maxWidth: '200px', marginTop: 2 }} />
                )}

                <div sx={{ display: 'flex', justifyContent: 'center', marginTop: 2 }}>
                    <a href="https://www.facebook.com/" target="_blank" rel="noopener" style={{ margin: 'auto', marginRight: '10px' }}>
                        <FacebookIcon color="primary" />
                    </a>
                    <a href="https://twitter.com/" target="_blank" rel="noopener" style={{ margin: 'auto', marginRight: '10px' }}>
                        <TwitterIcon color="primary" />
                    </a>
                    <a href="https://www.instagram.com/" target="_blank" rel="noopener" style={{ margin: 'auto' }}>
                        <InstagramIcon color="primary" />
                    </a>
                </div>
                <Typography variant="body2" color="textSecondary" align="center" sx={{ marginTop: 2 }}>
                    © {new Date().getFullYear()} UNPet. Todos los derechos reservados.
                </Typography>
            </CardContent>
        </Card>
    );
}





