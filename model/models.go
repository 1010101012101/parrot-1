package model

import "fmt"

type DocStorer interface {
	GetDoc(id int) (*Document, error)
	CreateDoc(doc *Document) error
	UpdateDoc(doc *Document) error
	DeleteDoc(id int) (int, error)
}

type ProjectStorer interface {
	GetProject(id int) (*Project, error)
	CreateProject(doc *Project) error
	// UpdateProject(doc *Project) error
	// DeleteProject(id int) (int, error)
}

func NewDocument(id int) *Document {
	return &Document{ID: id, Pairs: make(map[string]string)}
}

type Document struct {
	ID    int               `db:"id" json:"id"`
	Pairs map[string]string `db:"pairs" json:"pairs"`
}

// SyncKeys will add new keys from string slice t to document pairs.
// If additive is set to false, previous key/value pairs will be destroyed,
// and if set to true they will be kept.
func (d *Document) SyncKeys(t []string, additive bool) {
	if d.Pairs == nil || !additive {
		d.Pairs = make(map[string]string)
	}

	// Assign each key, if it's already there it will simply reassign to there
	// previous value, otherwise an empty string will be set
	for _, v := range t {
		d.Pairs[v] = d.Pairs[v]
	}
}

type Project struct {
	ID    int            `db:"id" json:"id"`
	Keys  []string       `db:"keys" json:"keys"`
	Langs map[string]int `db:"langs" json:"langs"`
}

func (p *Project) DocKey(lang string) (int, error) {
	v, ok := p.Langs[lang]
	if !ok {
		return 0, fmt.Errorf("no doc for lang key '%s'", lang)
	}
	return v, nil
}
