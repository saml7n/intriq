import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';
import { useNavigation } from '~/lib/NavigationContext';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import Navbar from '../shared/Navbar';
import { motion } from 'framer-motion';

interface DataSourceTypeCardProps {
  name: string;
  description: string;
  imgSrc: string;
  selected?: boolean;
  onClickHandler: () => void;
}

const detailsVariants = {
  intial: {
    opacity: 0,
    height: 0,
  },
  open: {
    opacity: 1,
    height: 'auto',
  },
  closed: {
    opacity: 0,
    height: 0,
  },
};

const DataSourceTypeCard: React.FC<DataSourceTypeCardProps> = ({
  name,
  description,
  imgSrc,
  selected,
  onClickHandler,
}) => {
  return (
    <div
      className={`card card-compact w-48 ${
        selected ? 'bg-base-100 border-secondary' : 'bg-base-200 border-base-200'
      } border hover:bg-base-100 hover:border-secondary shadow-xl cursor-pointer`}
      onClick={onClickHandler}
    >
      <figure>
        <img src={imgSrc} alt="logo" />
      </figure>
      <div className="card-body">
        <h2 className="card-title">{name}</h2>
        <p>{description}</p>
      </div>
    </div>
  );
};

function DataConnectAdd() {
  const { completedStep, setCompletedStep } = useNavigation();
  const [isSubmitDisabled, setIsSubmitDisabled] = useState<boolean>(true);
  const [selectedDataSourceType, setSelectedDataSourceType] = useState<string | null>(null);
  const navigate = useNavigate();
  function onSubmitClickHandler(event: any): void {
    if (completedStep < 2) setCompletedStep(2);
    navigate('/connect-data');
  }

  function onAbortClickHandler(event: any): void {
    navigate('/connect-data');
  }

  return (
    <>
      <Head title="Add a new Data Source" />
      <Navbar />
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 xl:col-span-4 z-10">
          <div className="form-control">
            <div className="flex flex-wrap items-center gap-2">
              <DataSourceTypeCard
                name="SAP Connector"
                description="v2 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SAP'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SAP');
                }}
              />
              <DataSourceTypeCard
                name="Sage Connector"
                description="v42 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'Sage'}
                onClickHandler={() => {
                  setSelectedDataSourceType('Sage');
                }}
              />
              <DataSourceTypeCard
                name="file"
                description="v2 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'File'}
                onClickHandler={() => {
                  setSelectedDataSourceType('File');
                }}
              />
              <DataSourceTypeCard
                name="SAP Connector"
                description="v2 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SAP'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SAP');
                }}
              />
              <DataSourceTypeCard
                name="SAP Connector"
                description="v2 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SAP'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SAP');
                }}
              />
              <DataSourceTypeCard
                name="SAP Connector"
                description="v2 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SAP'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SAP');
                }}
              />
            </div>
          </div>
          <hr className="my-6 border-t-2 border-base-content/5" />
          <motion.section initial={false} animate={selectedDataSourceType === 'SAP' ? 'open' : 'closed'} variants={detailsVariants} className="col-span-12 xl:col-span-4 overflow-hidden">
            <div className="form-control">
              <label className="label">
                <span className="label-text">SAP Server URL</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">SAP API token</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
          </motion.section>
          <motion.section initial={false} animate={selectedDataSourceType === 'Sage' ? 'open' : 'closed'} variants={detailsVariants} className="col-span-12 xl:col-span-4 overflow-hidden">
            <div className="form-control">
              <label className="label">
                <span className="label-text">Sage Server URL</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Sage API token</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
          </motion.section>
          <motion.section initial={false} animate={selectedDataSourceType === 'File' ? 'open' : 'closed'} variants={detailsVariants} className="col-span-12 xl:col-span-4 overflow-hidden">
            <div className="form-control">
              <label className="label">
                <span className="label-text">File Server URL</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">File API token</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
          </motion.section>
          {selectedDataSourceType && <hr className="my-6 border-t-2 border-base-content/5" />}
          <div className="form-control">
            <div className="flex items-center gap-2">
              <button className="btn btn-outline btn-error w-1/3" onClick={onAbortClickHandler}>
                Abort
              </button>
              <button
                className={`btn ${selectedDataSourceType ? 'btn-primary' : 'btn-disabled'} w-2/3`}
                onClick={onSubmitClickHandler}
              >
                Add new Data Source
              </button>
            </div>
          </div>
        </section>
      </div>
    </>
  );
}

export default DataConnectAdd;