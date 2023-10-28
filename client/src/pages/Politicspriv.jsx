import {Legal} from '../components/LegalInfo';
export function PoliticsPriv() {
    const title = 'Políticas de pivacidad';
    const descriptionURL = 'PoliticsPriv'
    return (
        <Legal title={title} descriptionMD={descriptionURL} imageUrl={'/app-img-unpetlogo.PNG'}/>
    );
};

export default PoliticsPriv;