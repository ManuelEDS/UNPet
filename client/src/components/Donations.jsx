// eslint-disable-next-line no-unused-vars
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import { Link } from 'react-router-dom'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import PaidIcon from '@mui/icons-material/Paid';

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';

export function Donations() {
  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="md">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Card sx={{ margin: 'auto', marginTop: 8, boxShadow: 4 , width:700, height:'auto'}}>
            <CardContent>
              <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <PaidIcon sx={{ fontSize: 80 }}>
                </PaidIcon>
                <Typography component="h1" variant="h4" sx={{ mt: 4, mb: 2, fontSize: 24, textAlign: 'center' }}>
                  Ayúdanos a dar más oportunidades
                </Typography>
              </Box>
              <Box sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
              }}>
                <Grid container spacing={4}>
                  <Grid item xs={12} sm={6}>
                    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                      <a href="https://paypal.me/UNPetDonaciones" target="_blank" rel="noopener noreferrer">
                        <img src={'paypal.png?url'} alt="Paypal" width="200" height="200" />
                      </a>
                    </Box>
                  </Grid>
                  <Grid item xs={12} sm={6}>
                    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                      <img src={'nequi.png?url'} alt="Nequi" width="200" height="200" />
                      <Typography variant="subtitle1" sx={{ mt: 2 }}>
                        Nequi - Juan Ramirez
                      </Typography>
                    </Box>
                  </Grid>
                </Grid>
              </Box>
            </CardContent>
          </Card>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
