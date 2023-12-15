import React, { ReactElement } from 'react';
import { Suspense } from 'react-lazy-no-flicker';

// This will show the animation
const Loader: React.FC = () => {
  return (
    <div className="position-fixed w-100 top-0 start-0 zindex-9999 bg-primary">
      <div style={{height: "3px"}} />
    </div>
  );
};

type LoadableProps = {
  // Define any additional props your component may accept
};

const Loadable = <P extends LoadableProps>(
  Component: React.ComponentType<P>
): React.FC<P> => (props: P): ReactElement => (
  <Suspense fallback={<Loader />}>
    <Component {...props} />
  </Suspense>
);

export default Loadable;