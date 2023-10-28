import {Legal} from '../components/LegalInfo';
export function TermsCond() {
    const title = 'Términos y Condiciones';
    const descriptionURL = 'TermsCond'
    return (
        <Legal title={title} descriptionMD={descriptionURL} imageUrl={'/app-img-unpetlogo.PNG'}/>
    );
};

export default TermsCond;
