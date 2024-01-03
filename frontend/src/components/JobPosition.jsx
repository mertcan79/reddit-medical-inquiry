import React from 'react';
import PropTypes from 'prop-types';
import { Badge } from 'UI/Badge';
import { Card } from 'UI/Card';
import { Stack } from 'UI/Stack';

const JobPosition = ({
  drugs = [],
  symptoms = [],
  gender,
  age,
  diagnosis,
  handleAddFilter,
}) => {
  const badges = diagnosis.length > 0 ? [diagnosis] : [];

  return (
    <Card>
      <div className='job-position'>
        <div className='job-position-info'>
          <div className='job-position-body'>
            <h2 className='job-position-title'>{`Age: ${age}, Gender: ${gender}`}</h2>
            <Stack>
              <div className='job-position-meta'>
                {`Drugs: ${drugs.join(', ')}`}
              </div>
              <br></br>
              <div className='job-position-meta'>
                {`Symptoms: ${symptoms.join(', ')}`}
              </div>
            </Stack>
          </div>
        </div>
        <Stack>
          {badges.map((item, index) => (
            <Badge
              key={index}
              onClick={() => handleAddFilter(item)}>
              {item}
            </Badge>
          ))}
        </Stack>
      </div>
    </Card>
  );
};

JobPosition.propTypes = {
  drugs: PropTypes.arrayOf(PropTypes.string),
  symptoms: PropTypes.arrayOf(PropTypes.string),
  gender: PropTypes.string,
  age: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  diagnosis: PropTypes.string,
  handleAddFilter: PropTypes.func,
};

export { JobPosition };