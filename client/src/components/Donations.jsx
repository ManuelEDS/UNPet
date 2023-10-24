// eslint-disable-next-line no-unused-vars
import * as React from 'react';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import CssBaseline from '@mui/material/CssBaseline';
import { Link } from 'react-router-dom'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import nequi from './nequi.png'
import paypal from './paypal.png'
import PaidIcon from '@mui/icons-material/Paid';

// TODO remove, this demo shouldn't need to reset the theme.

const defaultTheme = createTheme();

export function Donations() {
  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <PaidIcon>
          </PaidIcon>
          <Typography component="h1" variant="h5">
            Ayúdanos a dar más oportunidades
          </Typography>
          <Box sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
            <Grid container>
              <Grid item xs>
                <img src={paypal} width="300" height="300"></img>
              </Grid>
              <Grid sx={{
                alignItems: 'center',
              }} item xs>
                <Link to="https://paypal.me/UNPetDonaciones">
                  UNPetDonaciones
                </Link>
              </Grid>
              <Grid item xs>
                <img src={nequi} width="300" height="300"></img>
              </Grid>
              <Grid item>
                Nequi - Juan Ramirez
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
