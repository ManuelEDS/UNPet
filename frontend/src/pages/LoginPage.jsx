// eslint-disable-next-line no-unused-vars
import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import { Link } from 'react-router-dom'
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
//import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import {login, getUser, getProfile} from '../api/accounts.api'
import { useNavigate } from "react-router-dom";
import { useState } from 'react';

// TODO remove, this demo shouldn't need to reset the theme.
// import SearchBar from '../components/SearchBar';
// import User from '../components/User';
const defaultTheme = createTheme();

  export function Login() {
    const navigate = useNavigate();
    const [error, setError] = useState(false);

    const handleSubmit = async (event) => {
      event.preventDefault();
      const data = new FormData(event.currentTarget);
      console.log({
        userID: data.get('userID'),
        password: data.get('password'),
      });

      const resp = await login(data);
      //console.log(resp.data, resp);
      if (resp.status === 200) {
        navigate('/home');
      } else {
        setError(true);
        console.log('Login failed: ', resp.data.error, resp.status);
      }
    };

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
            <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
              <img src="/user-img-default.png" alt="User" width="40" height="40" />
            </Avatar>
            <Typography component="h1" variant="h5">
              Ingresar
            </Typography>
            <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Correo Electrónico o nombre de usuario (username)"
                name="userID"
                autoComplete="email"
                autoFocus
                error={error}
                helperText={error ? 'Credenciales incorrectas' : ''}
              />
              <TextField
                  required
                  fullWidth
                  name="password"
                  label="Contraseña"
                  type="password"
                  id="password"
                  autoComplete="new-password"
                  error={error}
                  helperText={error ? 'Credenciales incorrectas' : ''}
                />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Ingresar
              </Button>
              <Grid container>
                <Grid item xs>
                  <Link to="/password">
                    Olvidaste tu contraseña?
                  </Link>
                </Grid>
                <Grid item>
                  <Link to="/register">
                    {"No tienes una cuenta? Regístrate"}
                  </Link>
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Container>
      </ThemeProvider>
    );
  }
