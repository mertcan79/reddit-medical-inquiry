import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addPositions } from './store/positions/position-actions';
import { FilterPanel } from 'components/FilterPanel';
import { JobList } from 'components/JobList';
import { TheHeader } from 'components/TheHeader';

function App() {
  const dispatch = useDispatch();
  const positions = useSelector((state) => state.positions);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5002/processed-results');
      const result = await response.json();

      // Ensure 'data' property exists and is an array
      const positions = result.data && Array.isArray(result.data) ? result.data : [];

      dispatch(addPositions(positions));
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <>
      <TheHeader title="Extraction of medication&symptoms of posts from AskDocs subreddit and a possible diagnosis" />
      <div className='container'>
        <FilterPanel />
        <JobList />
      </div>
    </>
  );
}

export default App;
