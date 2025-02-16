import { useContext } from 'react';
import Breadcrumb from 'react-bootstrap/Breadcrumb';

import { CurrentPage } from '../Contexts/CurrentPageContext';

const Breadcrumbs = ({ list }) => {
  const { currentPage, setCurrentPage } = useContext(CurrentPage)
  const listItems = list.map((item, i) => {
    const  { name, change, active } = item

    return (
    <Breadcrumb.Item 
      onClick={e => setCurrentPage(change)}
      active={!active}
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