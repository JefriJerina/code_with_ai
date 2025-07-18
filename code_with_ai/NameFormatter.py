from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class NameFormatter:
    def __init__(self):
        """Initialize with Hugging Face embedding model."""
        print("Loading Hugging Face model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Define name formats with descriptions
        self.formats = {
            'first_last': {
                'template': '{first} {last}',
                'description': 'casual introduction business card everyday conversation',
                'example': 'John Smith'
            },
            'last_first': {
                'template': '{last}, {first}',
                'description': 'formal directory alphabetical listing official document',
                'example': 'Smith, John'
            },
            'first_initial': {
                'template': '{first_initial}. {last}',
                'description': 'professional signature author name abbreviated format',
                'example': 'J. Smith'
            },
            'formal_title': {
                'template': '{title} {last}',
                'description': 'respectful address professional meeting formal communication',
                'example': 'Dr. Smith'
            },
            'academic': {
                'template': '{last}, {first_initial}.',
                'description': 'research paper academic citation scholarly reference',
                'example': 'Smith, J.'
            }
        }
        
        # Create embeddings for format descriptions
        self.format_embeddings = self._create_embeddings()
        print("Name Formatter ready!")
    
    def _create_embeddings(self):
        """Create embeddings for each format description."""
        descriptions = [info['description'] for info in self.formats.values()]
        return self.model.encode(descriptions)
    
    def parse_name(self, full_name):
        """Parse name into components."""
        parts = full_name.strip().split()
        
        # Handle titles
        title = ""
        if parts and parts[0].lower().rstrip('.') in ['dr', 'prof', 'mr', 'mrs', 'ms']:
            title = parts[0]
            parts = parts[1:]
        
        # Extract components
        first = parts[0] if parts else ""
        last = parts[-1] if len(parts) > 1 else ""
        first_initial = first[0].upper() if first else ""
        
        return {
            'first': first,
            'last': last,
            'first_initial': first_initial,
            'title': title
        }
    
    def find_best_format(self, context):
        """Find the best format using embedding similarity."""
        # Create embedding for user's context
        context_embedding = self.model.encode([context])
        
        # Calculate similarities
        similarities = cosine_similarity(context_embedding, self.format_embeddings)[0]
        
        # Find best match
        best_idx = np.argmax(similarities)
        format_names = list(self.formats.keys())
        
        return format_names[best_idx], similarities[best_idx]
    
    def format_name(self, full_name, format_type):
        """Format a name using specified format."""
        components = self.parse_name(full_name)
        template = self.formats[format_type]['template']
        
        try:
            return template.format(**components)
        except KeyError:
            return "Format not applicable"
    
    def get_all_formats(self, full_name):
        """Get name in all available formats."""
        results = {}
        for format_name, format_info in self.formats.items():
            formatted = self.format_name(full_name, format_name)
            results[format_name] = {
                'formatted': formatted,
                'example': format_info['example']
            }
        return results
    
    def smart_format(self, full_name, context):
        """Automatically choose best format based on context."""
        best_format, confidence = self.find_best_format(context)
        formatted_name = self.format_name(full_name, best_format)
        
        return {
            'formatted_name': formatted_name,
            'format_used': best_format,
            'confidence': confidence
        }


def main():
    """Simple demonstration of the Name Formatter."""
    formatter = NameFormatter()
    
    print("\n=== Simple Name Formatter with Hugging Face Embeddings ===\n")
    
    # Test name
    test_name = "Dr. John Smith"
    
    print(f"Original name: {test_name}")
    print("-" * 50)
    
    # Show all formats
    all_formats = formatter.get_all_formats(test_name)
    for format_name, info in all_formats.items():
        print(f"{format_name:15} | {info['formatted']:20} | Example: {info['example']}")
    
    print("\n=== Smart Format Suggestions ===\n")
    
    # Test different contexts
    contexts = [
        "I need to write a research paper",
        "I'm introducing someone at a business meeting", 
        "I need to create a phone directory",
        "I'm addressing a formal letter"
    ]
    
    for context in contexts:
        result = formatter.smart_format(test_name, context)
        print(f"Context: {context}")
        print(f"Best format: {result['format_used']} -> {result['formatted_name']}")
        print(f"Confidence: {result['confidence']:.3f}\n")
    
    # Interactive mode
    print("=== Try It Yourself ===")
    print("Enter a name and context (or 'quit' to exit)")
    
    while True:
        name = input("\nEnter name: ").strip()
        if name.lower() == 'quit':
            break
            
        context = input("Enter context: ").strip()
        if context.lower() == 'quit':
            break
        
        if name and context:
            result = formatter.smart_format(name, context)
            print(f"→ {result['formatted_name']} (using {result['format_used']})")
    
    print("Thanks for using Name Formatter!")


if __name__ == "__main__":
    main()