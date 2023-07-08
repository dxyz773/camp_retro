function Search({ search, onSearch }) {
  return (
    <input
      placeholder="Search..."
      value={search}
      onChange={(e) => onSearch(e)}
    />
  );
}

export default Search;
