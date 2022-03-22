# Frontend Design & Resources

## Reactjs Notes

- `useState`
  - `const [value, setValue] = useState(initialValue);`
  - For expensive initial values:
    - `const [value, setValue] = useState(() => { return initialState; });`
  - The setter function **replaces** the old value so use function var to keep
    unchanged variables:

    ```js
    setValue(state => {
        return {
        ...state,
        property: newValue
        };
    });
    ```

  - Generally get old value in the setter instead of using global scope to derive old value.
- `useReducer`
  - Used when multiple state values need to be modified.
  - `const [state, dispatch] = useReducer(reducer, initialState);`
  - Implement the `reducer (state, action)` function first.
    - Generally uses the properties of the action object (E.g. `action.type: str`) to return a new state.
    - Uses `switch` statements with a default case.
  - For expensive init `const [state, dispatch] = useReducer(reducer, initArg, initFunc);`.
  - `dispatch(action)` is used to invoke/run the reducer within a given component.
    - E.g. `dispatch({ type: "SET_NAME", payload: "Jamal" });`
  - React always returns the same dispatch function for a particular call to useReducer
    within a component. (
    - If the dispatch function changed between calls,
      it could cause unnecessary re-renders when passed as a prop or included as a
      dependency for other hooks.
- `useEffect`
  - Hook to run/invoke code based on a component's lifecycle. E.g. after rendering/mounting.
  - Syntax:

    ```js
    useEffect(() => {
    // perform effect
    return () => {/*clean-up*/};
    }, [dep1, dep2]);
    ```

  - Be mindful of dep array. Use empty when the computation is expensive.
  - Return a cleanup function if allocating resources. E.g. Creating listners.
    - Example of event listner for window resize:

      ```js
        useEffect(() => {
            function handleResize () {
              setSize(getSize());
            }
            window.addEventListener('resize', handleResize);
        }, []);
      ```

  - Use case: When used with local storage and `useState`, can persist selection across reloads.

## Resources

### Pending

- React.js full overview <https://medium.com/madhash/react-components-classes-lifecycle-methods-simplified-a82d85c4bb10>
- developer learning <https://roadmap.sh/react>
- <https://github.com/tiaanduplessis/awesome-react-talks>
- React boilerplate and libs <https://landof.dev/awesome/react/>
- react beginner pair programming: <https://www.youtube.com/watch?v=G-aO5hzo1aw>
- <https://landof.dev/awesome/react/>
- <https://reactpatterns.com/>
- boilerplates:
  - <https://github.com/flavienbwk/reactjs-flask-ldap-boilerplate>
  - playlist: <https://www.youtube.com/playlist?list=PLEt8Tae2spYkfEYQnKxQ4vrOULAnMI1iF>
- mocks and testing <https://www.valentinog.com/blog/fake/>

### Done

- 2017 UI frameworks and tools <https://www.youtube.com/watch?v=AjzyV8BraIs>
  - multiple browser test during dev <https://browsersync.io/>
- State of UI dev in 2021 <https://www.youtube.com/watch?v=HgJ0S_9R8ek>
  - Tailwind CSS for productivity.
  - Jest for reactjs UTS.
  - Cypress for dev friendly UT with live browser dashboard.
  - Prettier for linting.
  - Storybook for developing components in isolation with immediate UI feedback.
  - Transpilation. I.e. converting newer JS features to downward-compatible code.
  - Bundeling (e.g. Parcel) converts app and css to one file each.
  - esbuild: golang implemented fast JS bundler.
