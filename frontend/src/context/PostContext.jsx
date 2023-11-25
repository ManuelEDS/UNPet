// import React, { createContext, useState, useEffect } from "react";
// import PropTypes from 'prop-types';
// import { getPost } from '../api/posts.api';
// export const PostContext = createContext();
// export const PostContextProvider = ({ children, idpublicacion }) => {
//     const [post, setPost] = useState(null);
//     const [loading, setLoading] = useState(true);

//     useEffect(() => {
//         const fetchPost = async () => {
//             if (idpublicacion) {
//                 try {
//                     setLoading(true);
//                     const response.data = await getPost(idpublicacion)
//                     const data = response.data.post
//                     if (data) {
//                         setPost({...data, username: data.nombreorganizacion.match(/\(([^)]+)\)$/)[1], fechapublicacion: new Date(data.fechapublicacion).toLocaleDateString()});
//                     } else {
//                         console.log('La respuesta no tiene datos');
//                     }
//                 } catch (error) {
//                     console.log(error);
//                 } finally {
//                     setLoading(false);
//                 }
//             }
//         };
//         fetchPost();
//     }, [idpublicacion]);

//     if (loading) {
//         return 'Cargando...'; // O puedes retornar cualquier componente de carga que prefieras
//     }
//     useEffect(() => {
//         console.log('datos2:', post);
//     }, [post]);
//     return (
//         <PostContext.Provider value={{ post, setPost }}>
//             {children}
//         </PostContext.Provider>
//     );
// };

// PostContextProvider.propTypes = {
//     children: PropTypes.node.isRequired,
// };

