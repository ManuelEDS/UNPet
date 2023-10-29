
import { getMD } from '../api/accounts.api';
import { useState, useEffect } from 'react';

export function GetMDText(filename) {
  const [markdownContent, setMarkdownContent] = useState('');

  useEffect(() => {
    getMD(`${filename}.md`).then((content) => {
      setMarkdownContent(content);
    });
  }, [filename]);

  return markdownContent;
}
export default GetMDText;


