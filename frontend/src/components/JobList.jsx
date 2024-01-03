import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { JobPosition } from './JobPosition';
import { selectFilters } from 'store/filters/filter-selectors';
import { addFilter } from 'store/filters/filter-actions';

const JobList = () => {
  const dispatch = useDispatch();
  const currentFilters = useSelector(selectFilters);
  const positions = useSelector((state) => state.positions);

  const handleAddFilter = (filter) => {
    dispatch(addFilter(filter));
  };

  return (
    <div className='job-list'>
      {Array.isArray(positions) &&
        positions.map((item) => (
          <JobPosition key={item.id} handleAddFilter={handleAddFilter} {...item} />
        ))}
    </div>
  );
};

export { JobList };
