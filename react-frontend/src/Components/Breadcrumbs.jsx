import { useContext } from 'react';
import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { CurrentPage } from '../Contexts/CurrentPageContext';

const Breadcrumbs = ({ list }) => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const listItems = list.map((item, i) => {
    const  { name, change } = item
    console.log(i, list.length - 1, i === list.length - 1, name)
    return (
    <Breadcrumb.Item 
      onClick={e => setCurrentPage(change)}
      active={i === list.length - 1}
      key={`breadcrumb-${name}`}
    >
      {name}
    </Breadcrumb.Item>
    )
  })

  return (
    <Breadcrumb>
      {listItems}
    </Breadcrumb>
  );
}

export default Breadcrumbs