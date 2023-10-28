
import {getMD} from '../api/accounts.api';
import React, { useState, useEffect } from 'react';


async function getLegal(filePath) {
    try {
      const response = await getMD(filePath)
      return response
    } catch (error) {
      console.error(`Error: ${error.message}`);
      return null;
    }
  }

  

  export function GetMDText() {
    const filename = 'TermsCond'
    const [markdownContent, setMarkdownContent] = useState('');
    useEffect(() => {
      getMD(filename+'.md').then((content) => {
        setMarkdownContent(content);
      });
    }, []);
    console.log('resultado: ', markdownContent);
    return (
    
        markdownContent
       
    );
}
export default GetMDText;


