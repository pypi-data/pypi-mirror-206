import React from 'react';
import { WidgetModel } from '@jupyter-widgets/base';
import { useModelMessenger, useModelState, WidgetModelContext } from './model';

interface WidgetProps {
  model: WidgetModel;
}

function ReactEditableTable(props: WidgetProps) {
  const [columns] = useModelState('columns');
  const [data, setData] = useModelState('data');
  const send = useModelMessenger();

  const rows = data.map((item, index) => {
    return (
      <tr key={index}>
        {columns.map((c) => (
          <td key={c.header}>
            {c.editable ? (
              <input
                type="text"
                value={item[c.accessor]}
                onChange={(e) => {
                  const data = { ...item, [c.accessor]: e.target.value };

                  setData((prev) => {
                    prev[index] = data;
                  });

                  send({
                    type: 'cell-changed',
                    payload: {
                      row: data,
                      index,
                    },
                  });
                }}
              />
            ) : (
              item[c.accessor]
            )}
          </td>
        ))}
      </tr>
    );
  });

  return (
    <div>
      <table>
        <thead>
          {columns.map((i) => (
            <th>{i.header}</th>
          ))}
        </thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  );
}

function withModelContext(Component: (props: WidgetProps) => JSX.Element) {
  return (props: WidgetProps) => (
    <WidgetModelContext.Provider value={props.model}>
      <Component {...props} />
    </WidgetModelContext.Provider>
  );
}

export default withModelContext(ReactEditableTable);
